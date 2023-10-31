#include "lists.h"

/**
 * check_cycle - A function that checks for the presence of a cycle
 * in a linked list.
 * @list: pointer to the linked list.
 * Return: Upon success 1, if there is a cycle, otherwise 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *speed, *slugish;

	if(!list || !list->next)
		return (0);
	speed = list;
	slugish = list;

	while(slugish != NULL && speed != NULL && speed->next != NULL)
	{
		slugish = slugish->next;
		speed = speed->next->next;
		if(slugish == speed)
		{
			return (1);
		}
	}
	return (0);
}
