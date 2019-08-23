
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
