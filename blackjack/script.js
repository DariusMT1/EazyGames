const suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs'];
const ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'];
const cardValues = {
    'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10
};

let deck, playerHand, dealerHand, playerScore, dealerScore, gameOver;
let playerMoney, currencySymbol;

document.getElementById('start-game').addEventListener('click', setupGame);
document.getElementById('hit').addEventListener('click', hit);
document.getElementById('stand').addEventListener('click', stand);
document.getElementById('restart').addEventListener('click', startGame);

function setupGame() {
    playerMoney = parseFloat(document.getElementById('money').value);
    currencySymbol = document.getElementById('currency').value;
    document.getElementById('setup').style.display = 'none';
    document.getElementById('game').style.display = 'block';
    startGame();
}

function startGame() {
    deck = createDeck();
    shuffleDeck(deck);
    playerHand = [];
    dealerHand = [];
    playerScore = 0;
    dealerScore = 0;
    gameOver = false;

    playerHand.push(dealCard());
    playerHand.push(dealCard());
    dealerHand.push(dealCard());
    dealerHand.push(dealCard());

    updateScores();
    updateUI();
}

function createDeck() {
    let deck = [];
    for (let suit of suits) {
        for (let rank of ranks) {
            deck.push({ suit, rank });
        }
    }
    return deck;
}

function shuffleDeck(deck) {
    for (let i = deck.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [deck[i], deck[j]] = [deck[j], deck[i]];
    }
}

function dealCard() {
    return deck.pop();
}

function calculateScore(hand) {
    let score = 0;
    let hasAce = false;
    for (let card of hand) {
        score += cardValues[card.rank];
        if (card.rank === 'A') {
            hasAce = true;
        }
    }
    if (hasAce && score + 10 <= 21) {
        score += 10;
    }
    return score;
}

function updateScores() {
    playerScore = calculateScore(playerHand);
    dealerScore = calculateScore(dealerHand);
}

function updateUI() {
    document.getElementById('player-cards').innerHTML = '';
    document.getElementById('dealer-cards').innerHTML = '';

    for (let card of playerHand) {
        const cardDiv = document.createElement('div');
        cardDiv.className = 'card';
        cardDiv.textContent = `${card.rank} of ${card.suit}`;
        document.getElementById('player-cards').appendChild(cardDiv);
    }

    for (let card of dealerHand) {
        const cardDiv = document.createElement('div');
        cardDiv.className = 'card';
        cardDiv.textContent = `${card.rank} of ${card.suit}`;
        document.getElementById('dealer-cards').appendChild(cardDiv);
    }

    document.getElementById('player-score').textContent = `Score: ${playerScore}`;
    document.getElementById('dealer-score').textContent = `Score: ${dealerScore}`;
    document.getElementById('player-money').textContent = `Money: ${currencySymbol}${playerMoney.toFixed(2)}`;

    if (gameOver) {
        document.getElementById('hit').disabled = true;
        document.getElementById('stand').disabled = true;
    } else {
        document.getElementById('hit').disabled = false;
        document.getElementById('stand').disabled = false;
    }

    if (playerScore > 21) {
        document.getElementById('message').textContent = 'You busted! Dealer wins.';
        playerMoney -= 10; // Deduct bet amount
        gameOver = true;
    } else if (dealerScore > 21) {
        document.getElementById('message').textContent = 'Dealer busted! You win.';
        playerMoney += 10; // Add bet amount
        gameOver = true;
    } else if (gameOver) {
        if (playerScore > dealerScore) {
            document.getElementById('message').textContent = 'You win!';
            playerMoney += 10; // Add bet amount
        } else if (playerScore < dealerScore) {
            document.getElementById('message').textContent = 'Dealer wins.';
            playerMoney -= 10; // Deduct bet amount
        } else {
            document.getElementById('message').textContent = 'It\'s a tie!';
        }
    } else {
        document.getElementById('message').textContent = '';
    }
}

function hit() {
    if (!gameOver) {
        playerHand.push(dealCard());
        updateScores();
        updateUI();
        if (playerScore > 21) {
            gameOver = true;
            updateUI();
        }
    }
}

function stand() {
    if (!gameOver) {
        while (dealerScore < 17) {
            dealerHand.push(dealCard());
            updateScores();
        }
        gameOver = true;
        updateUI();
    }
}

startGame();
