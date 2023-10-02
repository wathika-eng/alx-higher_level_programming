#include "lists.h"

/**
 *  check_cycle - checks if a linked list contains a cycle
 *  @list: linked list to check
 *  Return: 1 success else 0
*/

int check_cycle(listint_t *list)
{
	listint_t *al = list;
	listint_t *bl = list;

	if (!list)
	{
		return (0);
	}
	while (al &&bl && al->next)
	{
		bl = bl->next;
		al = al->next->next;
		if (al == bl)
		{
			return (1);
		}
		else
		{
			return (0);
		}
	}
	return (0);
}
