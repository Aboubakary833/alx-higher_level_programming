#include "lists.h"

/**
 * check_cycle - Check if a single list has a cycle
 * @list: Signle list
 * Return: 1 if found or 0
 */
int check_cycle(listint_t *list)
{
listint_t *cpy = list;
listint_t *tmp = list;
while (cpy && tmp && cpy->next)
{
	tmp = tmp->next;
	cpy = cpy->next->next;
	if (tmp->next->n == cpy->n)
		return (1);
}
return (0);
}
