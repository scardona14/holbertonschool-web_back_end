export default function taskBlock(trueOrFalse) {
    const task = false;
    const task2 = true;

    if (trueOrFalse) {
        /* eslint-disable no-console */
        const task = true;
        const task2 = false;
    }

    return [task, task2];
}