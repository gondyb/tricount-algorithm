# Tricount algorithm

Python implementatio of the [Tricount](https://www.tricount.com/)'s algorithm.

The goal of this algorithm is to omptimize the amount of transactions in a group of friends where each other owes each other money.

In my implementation:
* Benjamin owes 10 € to Gaston, 20 € to Valentin and 50 € to Theo
* Valentin owes 30 € to Benjamin, 90 € to Gaston and 40 € to Theo
* Gaston owes 70 € to Benjamin, 35 € to Valentin and 20 € to Theo
* Theo owes 10 € to Benjamin, 30 € to Valentin and 20 € to Gaston

When we run the script, we can see that in the end, only three transactions are needed:
* Valentin owes Theo 50 €
* Valentin owes Benjamin 30 €
* Valentin owes Gaston 5 €