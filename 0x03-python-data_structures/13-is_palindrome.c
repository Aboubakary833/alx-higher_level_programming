#include "lists.h"

/**
 * is_palindrome - Check if a singly linked list is a palindrome
 * @head: The list head
 * Return: 1 if the list is a palindrome or 0 if not
*/
int is_palindrome(listint_t **head)
{
listint_t *current, *reversed, *tmp;
if ((*head) == NULL)
	return (1);
current = (*head);
while (current != NULL)
{
	if (reversed == NULL)
	{
		reversed->n = current->n;
		reversed->next = NULL;
		current = current->next;
	}
	else
	{
		tmp = current->next;
		current->next = reversed;
		reversed = current;
		current = tmp;
	}
}
while (reversed != NULL && current != NULL)
{
	if (reversed->n != current->n)
		return (0);
	reversed = reversed->next;
	current = current->next;
}
return (1);
}
