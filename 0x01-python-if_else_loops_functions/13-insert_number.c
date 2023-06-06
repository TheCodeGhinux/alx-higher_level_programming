#include "lists.h"

/**
 * insert_node - It inserts a number into a sorted singly-linked list.
 * @head: Pointer to the head of the linked list.
 * @number: The number to insert.
 *
 * Return: the address of the new node,
 *          NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nd = *head, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (nd == NULL || nd->n >= number)
	{
		new_node->next = nd;
		*head = new_node;
		return (new_node);
	}

	while (nd && nd->next && nd->next->n < number)
		nd = nd->next;

	new_node->next = nd->next;
	nd->next = new_node;

	return (new_node);
}
