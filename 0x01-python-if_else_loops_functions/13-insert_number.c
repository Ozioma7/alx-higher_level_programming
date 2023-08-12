#include "lists.h"

/**
 * insert_node - Node to be inserted
 * @head: Head of node
 * @number: where to insert the node
 * Result: NULL or answer
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *newNode;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;

	if (node == NULL || node->n >= number)
	{
		newNode->next = node;
		*head = newNode;
		return (newNode);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	newNode->next = node->next;
	node->next = newNode;
}
