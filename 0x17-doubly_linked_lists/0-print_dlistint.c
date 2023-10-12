#include "lists.h"
#include <stdio.h>

/**
  * print_dlistint - print integers in the doubly linked list.
  * @h: point to the first node.
  * 
  * Return: counting num of nodes.
  */
size_t print_dlistint(const dlistint_t *h)
{
	dlistint_t *tmp;
	size_t count = 0;

	if (h == NULL)
		return (count);
	tmp = (dlistint_t *)h;
	while (tmp != NULL)
	{
		printf("%d\n", tmp->n);
		tmp = tmp->next;
		count++;
	}
	return (count);
}
