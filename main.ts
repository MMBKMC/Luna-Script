// luna script

export enum TokenType{
    Number,
    Put,
    console,
    FLOAT,
    A,
    Y,
    X
}

export interface Token {
    value: string,
    type: TokenType,
}