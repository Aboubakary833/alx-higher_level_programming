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
listint_t *new, *current, *next;
new = malloc(sizeof(struct listint_s));
if (new == NULL)
	return (NULL);
new->n = number;
current = *head;
if (current->n > number)
{
	new->next = (*head);
	(*head) = new;
}
next = current->next;
while (current != NULL && next != NULL && next->n < number)
{
	current = next;
	next = current->next;
}
new->next = next;
current->next = new;
return (new);
}
