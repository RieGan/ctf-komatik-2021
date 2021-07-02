// docker run --rm -v $PWD:/pwd --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -d --name chal -i ubuntu:20.04
// docker exec -it chal bash
// apt update && apt install -y make gcc
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stdbool.h>
#include<signal.h>

int LENGTH = 24;

void kill_on_timeout(int sig) {
  if (sig == SIGALRM) {
    _exit(0);
  }
}


void nobaper() {
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
	signal(SIGALRM, kill_on_timeout);
	alarm(60);
}

bool check_length(char *password) {
    return(strlen(password) == LENGTH);
}

unsigned int process(char *substr) {
    unsigned int res = (int)substr[0] ^ (int)substr[1];
    res *= (int)substr[2];
    res += (int)substr[3];
    res ^= ((int)substr[0] * (int)substr[0] * (int)substr[0]);
    res *= (int)substr[0];
    res -= (int)substr[2];
    res %= 0xffffff;
    return res;
}

bool valid_inputs(char *first, char *second) {
    return check_length(first) && check_length(second) && strcmp(first, second);
}

int main() {
    nobaper();
    char first[LENGTH+1];
    char second[LENGTH+1];
    char result1[36] = "";
    char result2[36] = "";
    char *pos;

    fputs("First String: ", stdout);
    fgets(first, LENGTH+2, stdin);
    if ((pos=strchr(first, '\n')) != NULL)
        *pos = '\0';
    fputs("Second String: ", stdout);
    fgets(second, LENGTH+2, stdin);
    if ((pos=strchr(second, '\n')) != NULL)
        *pos = '\0';

    if(valid_inputs(first, second)) {
        for(int i=0; i<LENGTH/4; i++) {
            char to_be_processed[5];
            char tmp_result[7];
            memcpy(to_be_processed, &first[i*4], 4);
            to_be_processed[4] = '\0';
            sprintf(tmp_result, "%x", process(to_be_processed));
            tmp_result[6] = '\0';
            strcat(result1, tmp_result);
        }

        for(int i=0; i<LENGTH/4; i++) {
            char to_be_processed[5];
            char tmp_result[7];
            memcpy(to_be_processed, &second[i*4], 4);
            to_be_processed[4] = '\0';
            sprintf(tmp_result, "%x", process(to_be_processed));
            tmp_result[6] = '\0';
            strcat(result2, tmp_result);
        }

        if(!strcmp(result1, result2)) {
            system("cat flag.txt");
            return 0;
        }
    }
    puts("Boooo");
    return 1;
}