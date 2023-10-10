#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - start
 * @head: reverse.
 * Return: ptr
*/

listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;
	
	while (node)
	{
		next = node->next;
		node->next = prev;

		prev = node;
		node = next;
	}
	*head = prev;
	return (*head);
}
