
#include <stdio.h>
#include <string.h>

typedef struct{
    int i;
    double d;
    char str[17];
}Lib_Struct;

int fun(int i, double d)
{
    printf("-- fun -- %d , %lf\n", i, d);
    return i*2;
}

Lib_Struct fun_io_struct(Lib_Struct ls)
{
    static Lib_Struct local;

    printf("-- fun_io_struct -- %d, %lf, %s\n", ls.i, ls.d, ls.str);

    memcpy(&local, &ls, sizeof(Lib_Struct));
    local.i *= 2;
    local.d *= 2;
    int i;
    for(i = 0; i < 17; i++)
        local.str[i] += 1;
    
    return local;
}

Lib_Struct* fun_io_struct_point(Lib_Struct *ls)
{
    printf("-- fun_io_struct -- %d, %lf, %s\n", ls->i, ls->d, ls->str);

    ls->i *= 2;
    ls->d *= 2;
    int i;
    for(i = 0; i < 17; i++)
        ls->str[i] += 1;
    
    return ls;
}

//--- python + msg ---

#include <sys/ipc.h>
#include <sys/msg.h>

#define MSG_TYPE   1
#define MSG_PATH   "./"
#define MSG_ID_W   'W'
#define MSG_ID_R   'R'

typedef struct{
    int status;
    char cmd[16];
}Msg_Content;

typedef struct{
    long type;
    Msg_Content content;
}Msg_Struct;

static int msg_r = 0, msg_w = 0;

int msg_init(void)
{
    if(msg_r < 1)
    {
        key_t msg_key;
        if((msg_key = ftok(MSG_PATH, MSG_ID_R)) == -1){
            fprintf(stderr, "ftok r err\n");
            return 1;
        }if((msg_r = msgget(msg_key, IPC_CREAT|0666)) == -1){
            fprintf(stderr, "msgget r err\n");
            return 1;
        }
    }
    if(msg_w < 1)
    {
        key_t msg_key;
        if((msg_key = ftok(MSG_PATH, MSG_ID_W)) == -1){
            fprintf(stderr, "ftok w err\n");
            return 1;
        }if((msg_w = msgget(msg_key, IPC_CREAT|0666)) == -1){
            fprintf(stderr, "msgget w err\n");
            return 1;
        }
    }
    return 0;
}

int msg_read(Msg_Content *content)
{
    Msg_Struct msg;

    if(msg_r > 0 && 
        msgrcv(msg_r, &msg, sizeof(Msg_Content), 0, IPC_NOWAIT) != -1)
    {
        memcpy(content, &msg.content, sizeof(Msg_Content));
        return 1;
    }
    return 0;
}

void msg_write(Msg_Content content)
{
    Msg_Struct msg;
    msg.type = MSG_TYPE;
    memcpy(&msg.content, &content, sizeof(Msg_Content));
    if(msg_w > 0)
        msgsnd(msg_w, &msg, sizeof(Msg_Content), IPC_NOWAIT);
}