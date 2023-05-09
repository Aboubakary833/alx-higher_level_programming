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
listint_t *current = *head, *new;

new = malloc(sizeof(listint_t));
if (new == NULL)
{
return (NULL);
}
new->n = number;

if (current == NULL || current->n >= number)
{
new->next = current;
*head = new;
return (new);
}

while (current && current->next && current->next->n < number)
{
current = current->next;
}

new->next = current->next;
current->next = new;

return (new);
}
