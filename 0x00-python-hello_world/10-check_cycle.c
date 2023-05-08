#include "lists.h"

/**
 * check_cycle - Check if a single list has a cycle
 * @list: Signle list
 * Return: 1 if found or 0
*/
int check_cycle(listint_t *list)
{
listint_t *cpy_1 = list;
listint_t *cpy_2 = list;
listint_t *tmp = list;
while (cpy_1 && cpy_2)
{
	tmp = cpy_1->next;
	if (tmp)
	{
		cpy_2 = cpy_1->next;
		cpy_1 = tmp->next;
	}
	if (cpy_1 == cpy_2)
		return (1);
}
return (0);
}
