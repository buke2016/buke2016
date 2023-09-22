#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NUM_RANKS 13
#define NUM_SUITS 4
#define NUM_CARDS 52
#define HAND_SIZE 5

enum rank {ACE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING};
enum suit {CLUBS, DIAMONDS, HEARTS, SPADES};

struct card {
    enum rank rank;
    enum suit suit;
};

void print_card(struct card c) {
    switch (c.rank) {
        case ACE: printf("A"); break;
        case TWO: printf("2"); break;
        case THREE: printf("3"); break;
        case FOUR: printf("4"); break;
        case FIVE: printf("5"); break;
        case SIX: printf("6"); break;
        case SEVEN: printf("7"); break;
        case EIGHT: printf("8"); break;
        case NINE: printf("9"); break;
        case TEN: printf("10"); break;
        case JACK: printf("J"); break;
        case QUEEN: printf("Q"); break;
        case KING: printf("K"); break;
    }
    switch (c.suit) {
        case CLUBS: printf("C"); break;
        case DIAMONDS: printf("D"); break;
        case HEARTS: printf("H"); break;
        case SPADES: printf("S"); break;
    }
}

void print_hand(struct card hand[], int num_cards) {
    for (int i = 0; i < num_cards; i++) {
        print_card(hand[i]);
        printf(" ");
    }
    printf("\n");
}

void shuffle(struct card deck[], int num_cards) {
    srand(time(NULL));
    for (int i = 0; i < num_cards; i++) {
        int j = rand() % num_cards;
        struct card temp = deck[i];
        deck[i] = deck[j];
        deck[j] = temp;
    }
}

void swap_cards(struct card *card1, struct card *card2) {
    struct card temp = *card1;
    *card1 = *card2;
    *card2 = temp;
}

void sort_hand(struct card hand[], int num_cards) {
    for (int i = 0; i < num_cards - 1; i++) {
        for (int j = i + 1; j < num_cards; j++) {
            if (hand[j].rank < hand[i].rank) {
                swap_cards(&hand[i], &hand[j]);
            }
        }
    }
}

int get_rank_count(struct card hand[], int num_cards, enum rank r) {
    int count = 0;
    for (int i = 0; i < num_cards; i++) {
        if (hand[i].rank == r) {
            count++;
        }
    }
    return count;
}

int check_for_books(struct card hand[], int num_cards) {
    int books = 0;
    for (int i = 0; i < NUM_RANKS; i++) {
        if (get_rank_count(hand, num_cards, i) == 4) {
            books++;
        }
    }
    return books;
}

int main() {
    struct card deck[NUM_CARDS];
    int next_card = 0;
    for (int i = 0; i < NUM_RANKS; i++) {
        for (int j = 0; j < NUM_SUITS; j++) {
            deck[next_card].rank = i;
            deck[next_card].suit = j;
            next_card++;
        }
    }
    shuffle(deck, NUM_CARDS);

    struct card player_hand[HAND_SIZE];
    struct card computer_hand[HAND_SIZE];
    int num_player_cards = 0;
    int num_computer_cards = 0;

    // Deal initial hands.
    for (int i = 0; i < HAND_SIZE; i++) {
        player_hand[num_player_cards] = deck[next_card];
        num_player_cards++;
        next_card++;
        computer_hand[num_computer_cards] = deck[next_card];
        num_computer_cards++;
        next_card++;
    }

    int player_books = 0;
    int computer_books = 0;

    while (next_card < NUM_CARDS) {
        // Player's turn.
        printf("Your hand: ");
        print_hand(player_hand, num_player_cards);
        printf("Computer's hand: ");
        print_hand(computer_hand, num_computer_cards);
        enum rank player_guess;
        printf("Guess a rank (0=Ace, 1=2, ..., 12=King): ");
        scanf("%d", &player_guess);
        if (get_rank_count(computer_hand, num_computer_cards, player_guess) > 0) {
            printf("Computer has ");
            for (int i = 0; i < num_computer_cards; i++) {
                if (computer_hand[i].rank == player_guess) {
                    print_card(computer_hand[i]);
                    printf(" ");
                    player_hand[num_player_cards] = computer_hand[i];
                    num_player_cards++;
                    for (int j = i; j < num_computer_cards - 1; j++) {
                        computer_hand[j] = computer_hand[j + 1];
                    }
                    num_computer_cards--;
                    i--;
                }
            }
            printf("\n");
            if (get_rank_count(player_hand, num_player_cards, player_guess) == 4) {
                printf("You got a book!\n");
                player_books++;
            }
        } else {
            printf("Go fish!\n");
            player_hand[num_player_cards] = deck[next_card];
            num_player_cards++;
            next_card++;
            if (get_rank_count(player_hand, num_player_cards, player_guess) == 4) {
                printf("You got a book!\n");
                player_books++;
            }
        }
        if (num_player_cards == 0 || num_computer_cards == 0 || next_card == NUM_CARDS) {
            break;
        }

        // Computer's turn.
        enum rank computer_guess = rand() % NUM_RANKS;
        printf("Computer guesses %d\n", computer_guess);
        if (get_rank_count(player_hand, num_player_cards, computer_guess) > 0) {
            printf("You have ");
            for (int i = 0; i < num_player_cards; i++) {
                if (player_hand[i].rank == computer_guess) {
                    print_card(player_hand[i]);
                    printf(" ");
                    computer_hand[num_computer_cards] = player_hand[i];
                    num_computer_cards++;
                    for (int j = i; j < num_player_cards - 1; j++) {
                        player_hand[j] = player_hand[j + 1];
                    }
                    num_player_cards--;
                    i--;
                }
            }
            printf("\n");
            if (get_rank_count(computer_hand, num_computer_cards, computer_guess) == 4) {
                printf("Computer got a book");
            }
        }
    }
}