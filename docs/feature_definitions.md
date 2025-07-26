# Break and Retest Feature Definitions 
Updated: 07/23/2025

## 1. Strategy
- Description: We have two different types of *Break and Retest* (B/R) setups. B/R to the upside which is a long position and B/R to the downside which is a short position.
    - B/R Up
    - B/R Down

## 2. Liquidity Zone
- Description: The B/R by definition is a reaction off of only the NY Open liquidity zone. Also called the NY Open box or just box.
    - NY Open

## 3. Box High
- Description: This is the high of the 15-minute candle at 8:15 AM EST.

## 4. Box Low
- Description: This is the low of the 15-minute candle at 8:15 AM EST.

## 5. Box mid
- Description: This is the midpoint of the Box High and Box low.
- Formula: Box Mid = (Box High + Box Low) / 2

## 6. Box Width
- Description: This is the total number of points between Box High and Box Low.
- Formula: Box Width = Box High - Box Low

## 7. Break Initial Time
- Description: We define a "break" as a sequence of consecutive candles moving away from the NY Open Box boundary up to the candle with the highest high (or lowest low). *Break Initial Time* is the timestamp of the first 1-minute candle that exits the box’s edge, followed by consecutive candles closing outside the box.

## 8. Break Max
- Description: This is the last candle with the highest high (or lowest low) in the break.

## 9. Break Max Time
- Description: This is the timestamp of *Break Max*.

## 10. Break Magnitude Boundary
- Description: This is the total number of points between the boundary of the box and *break max*
- Formula: 
    - IF *Strategy* = B/R Up: 
        - *Break Magnitude Boundary* = *Break Max* - *Box High*
    - IF *Strategy* = B/R Down: 
        - *Break Magnitude Boundary* = *Box Low* - *Break Max*

## 11. Break Magnitude Mid
- Description: This is the total number of points between the midpoint of the box and *break max*
- Formula: 
    - IF *Strategy* = B/R Up: 
        - *Break Magnitude Mid* = *Break Max* - *Box Mid*
    - IF *Strategy* = B/R Down: 
        - *Break Magnitude Mid* = *Box Mid* - *Break Max*

## 12. Break Duration
- Description: This is the **inclusive** sum of all the 1-minute candles from *Break Initial Time* to *Break Max Time*. *Break Duration* is measured in minutes.
- Formula: Break Duration = (*Break Max Time* - *Break Initial Time*) + 1

## 13. Retest Initial Time
- Description: We define the "retest" as a sequence of consecutive candles that are within the NY Open box after the *Break Max* has occured. *Retest Initial Time* is the timestamp of the first 1-minute candle that touches the box's edge, followed by consecutive candles within the NY open box.









