#!/bin/env node

import { createInterface } from 'readline/promises';
import { readFileSync } from 'fs';
import { exit } from 'process';
const rl = createInterface({
  input: process.stdin,
  output: process.stdout
});

const duck = {
    canQuack: true,
    quack: () => {
        console.log('Quack.');
    },
    readFlag: () => {
        console.log(readFileSync('flag.txt', 'utf8'));
    }
};

const json = await rl.question('Please enter some JSON: ');
const obj = JSON.parse(json);

delete obj.canReadFlag;

Object.assign(duck, obj);

if (duck.canQuack) {
    duck.quack();
} else if (duck.canReadFlag) {
    duck.readFlag();
}

exit();
