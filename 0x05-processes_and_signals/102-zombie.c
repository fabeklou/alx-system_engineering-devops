#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - create an infinite loop
 *
 * Return: Always 0 (success)
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - entry point
 *
 * description: creates 5 zombie processes
 *
 * Return: Always 0 (success)
 */
int main(void)
{
	int i;
	pid_t process;

	for (i = 0; i < 5; i++)
	{
		process = fork();

		if (!process)
			return (0);

		printf("Zombie process created, PID: %d\n", process);
	}

	infinite_while();

	return (0);
}
