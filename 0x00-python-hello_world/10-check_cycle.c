#include "lists.h"

/**
 * check_cycle - Check if a single list has a cycle
 * @list: Signle list
 * Return: 1 if found or 0
*/
int check_cycle(listint_t *list)
{
listint_t *cpy = list;
listint_t *tmp;
while (cpy != NULL && cpy->next != NULL)
{
	tmp = cpy->next;
	while (tmp != NULL)
	{
		if (tmp->next->n == cpy->n)
			return (1);
		tmp = tmp->next;
	}
	cpy = cpy->next;
}
return (0);
}
