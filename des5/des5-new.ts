const createDeck = (cards: number): number[] => (
    Array.from({ length: cards }, (_, i) => (i + 1))
  )
  
  const outShuffleDeck = (deck: number[]): number[] => (
    deck.map((_, i, originalDeck) => (
      originalDeck[i % 2 === 0 ? i / 2 : Math.floor(i / 2) + originalDeck.length / 2]
    ))
  )
  
  const deckIsSorted = (deck: number[]): boolean => (
    deck.slice(1).every((value, i) => (value === i + 2))
  )
  
  const findSmallestDeckThatReturnsToSortedOrderAfterNOutShuffles = (outShuffles: number) => {
    let deckSize = 0
  
    nextDeck:
    while (true) {
      deckSize += 2
  
      let deck = createDeck(deckSize)
  
      for (let i = 0; i < outShuffles - 1; i++) {
        deck = outShuffleDeck(deck)
  
        if (deckIsSorted(deck)) {
          continue nextDeck;
        }
      }
  
      if (deckIsSorted(outShuffleDeck(deck))) {
        return deckSize
      }
    }
  }
  
  console.log(findSmallestDeckThatReturnsToSortedOrderAfterNOutShuffles(13))