#include "lists.h"

/**
 * check_cycle - that checks the cycle of a singly linked list
 * @list: a head pointer in the list
 *
 * Return: 0 for no cycle and 1 if it has
 */
int check_cycle(listint_t *list)
{

	listint_t *old;
	listint_t *tobe;

	old = list;
	tobe = list;

	while (list && tobe && tobe->next)
	{
		list = list->next;
		tobe = tobe->next->next;

		if (tobe == list)
		{
			list = old;
			old = tobe;
			while (true)
			{
				tobe = old;
				while (tobe->next != list && tobe->next != old)
				{
					tobe = tobe->next;
				}
				if (tobe->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}
return (0);
}
