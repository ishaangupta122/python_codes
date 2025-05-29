// Kansack Problem (Greedy Algorithm)

#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int weight;
    int value;
    float ratio;
} Item;

int compare(const void* a, const void* b) {
    Item* item1 = (Item*)a;
    Item* item2 = (Item*)b;
    if (item1->ratio < item2->ratio) return 1;
    else if (item1->ratio > item2->ratio) return -1;
    else return 0;
}

float fractionalKnapsack(int W, Item items[], int n) {
    qsort(items, n, sizeof(Item), compare);

    float totalValue = 0.0;

    for (int i = 0; i < n; i++) {
        if (W >= items[i].weight) {
            W -= items[i].weight;
            totalValue += items[i].value;
        } else {
            totalValue += items[i].ratio * W;
            break;
        }
    }

    return totalValue;
}

int main() {
    Item items[] = {
        {10, 60, 0},
        {20, 100, 0},
        {30, 120, 0}
    };
    int n = sizeof(items) / sizeof(items[0]);
    int W = 50;

    for (int i = 0; i < n; i++) {
        items[i].ratio = (float)items[i].value / items[i].weight;
    }

    printf("Maximum value (Fractional Knapsack): %.2f\n", fractionalKnapsack(W, items, n));
    return 0;
}
