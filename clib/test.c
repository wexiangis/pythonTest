#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>

//--- python + msg ---

#include <sys/ipc.h>
#include <sys/msg.h>

#define MSG_TYPE   1
#define MSG_PATH   "./"
#define MSG_ID_W   'R'
#define MSG_ID_R   'W'

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

void thread_read(void)
{
    Msg_Content content;

    while(1)
    {
        if(msg_read(&content))
            printf("thread_read: %d, %s\n", content.status, content.cmd);
        usleep(200000);
    }
}

int main(void)
{
    msg_init();

    pthread_t th;
    pthread_create(&th, NULL, (void*)&thread_read, NULL);

    char input[8] = {0};
    Msg_Content content = {
        .status = 200,
        .cmd = "msg from test",
    };
    
    while(1)
    {
        scanf("%s", input);
        msg_write(content);
        // msg_write(content);
        sleep(1);
    }
}
