#include "lists.h"
/**
 * check_cycle - check a cycle in a linked list
 * @list: linked list
 * Return: returns 1 if true o if no cycle
 */

int check_cycle(listint_t *list)
{
listint_t *current, *tmp;
current = tmp = list;
while (current != NULL)
{
while (tmp != current)
{
if (tmp == current->next)
return (1);
tmp = tmp->next;
}
tmp = list;
current = current->next;
}
return (0);
}
