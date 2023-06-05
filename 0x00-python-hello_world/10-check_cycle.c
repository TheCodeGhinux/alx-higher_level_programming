#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *c, *d;

	if (list == NULL || list->next == NULL)
		return (0);

	c = list->next;
	d = list->next->next;

	while (c && d && d->next)
	{
		if (c == d)
			return (1);

		c = c->next;
		d = d->next->next;
	}

	return (0);
}
