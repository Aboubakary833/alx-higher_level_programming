#include "lists.h"

/**
 * is_palindrome - Check if a singly linked list is a palindrome
 * @head: The list head
 * Return: 1 if the list is a palindrome or 0 if not
*/
int is_palindrome(listint_t **head)
{
listint_t *current, *reversed;
if ((*head) == NULL || (*head)->next)
	return (1);
current = (*head);
reversed = reverse_listint(head);
while (reversed != NULL && current != NULL)
{
	if (reversed->n != current->n)
		return (0);
	reversed = reversed->next;
	current = current->next;
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
