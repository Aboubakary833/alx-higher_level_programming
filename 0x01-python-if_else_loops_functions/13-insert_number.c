#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - Insert a new node into a single list
 * @head: Single list head
 * @number: New list item number
 * Return: The list
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new, *current;
new = malloc(sizeof(struct listint_s));
if (new == NULL)
	return (NULL);
new->n = number;
current = *head;
if (current == NULL || current->n == 0 || current->n >= number)
{
	new->next = (*head);
	(*head) = new;
	return (new);
}
while (current != NULL && current->next != NULL && current->next->n < number)
	current = current->next;
if (current != NULL)
{
	new->next = current->next;
	current->next = new;
}

return (new);
}
