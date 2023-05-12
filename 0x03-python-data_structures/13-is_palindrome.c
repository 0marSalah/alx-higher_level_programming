#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
    listint_t *current;
    int i, j, len;
    int array[10000];

    if (*head == NULL)
        return (1);

    current = *head;
    len = 0;
    while (current != NULL)
    {
        array[len] = current->n;
        current = current->next;
        len++;
    }

    for (i = 0, j = len - 1; i < len / 2; i++, j--)
    {
        if (array[i] != array[j])
            return (0);
    }
    return (1);
}
