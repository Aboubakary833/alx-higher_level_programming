#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - Check if a singly linked list is a palindrome
 * @head: The list head
 * Return: 1 if the list is a palindrome or 0 if not
*/
int is_palindrome(listint_t **head)
{
listint_t *current, *tmp, *reverse;
int len = 0, i = 0, first[10240], last[10240];
current = (*head);
while (current != NULL)
{
	len++;
	current = current->next;
}
if (len % 2 != 0)
	return (0);
current = (*head);
tmp = (*head);
reverse = reverse_listint(&tmp);
while (i < len / 2 && current != NULL && reverse != NULL)
{
	first[i] = current->n;
	last[i] = reverse->n;
	current = current->next;
	reverse = reverse->next;
	i++;
}

for (; i >= 0; i--)
{
	if (first[i] != last[i])
		return (0);
}
return (1);
}

/**
 * reverse_listint - Reverse a int list
 * @head: The list head
 * Return: Pointer to the first head
 */
listint_t *reverse_listint(listint_t **head)
{
listint_t *cur, *next;
while ((*head) != NULL)
{
	next = (*head)->next;
	(*head)->next = cur;
	cur = (*head);
	(*head) = next;
}
(*head) = cur;
return (*head);
}
