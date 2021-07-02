#include<stdio.h>
#include<stdlib.h>
#include<signal.h>
#include<string.h>

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

int main() {
  nobaper();

  char str[64];

  int byte_count = 45;
  char data[45];
  FILE *fp;
  fp = fopen("./flag.txt", "r");
  fread(&data, 1, byte_count, fp);
  fclose(fp);

  unsigned long int *p = &data;

  puts("*Something's not right here, I can smell it.*\n");
  write(1, "Input : ", 8);
  scanf("%63s", str);
  printf(str);

  return 1;
}