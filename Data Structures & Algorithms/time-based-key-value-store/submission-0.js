class TimeMap {
    constructor() {
        this.keyStore = new Map();
    }

    /**
     * @param {string} key
     * @param {string} value
     * @param {number} timestamp
     * @return {void}
     */
    set(key, value, timestamp) {
        const timestampArray = this.keyStore.has(key) ? this.keyStore.get(key) : [];
        timestampArray[timestamp] = value;
        this.keyStore.set(key, timestampArray);
    }

    /**
     * @param {string} key
     * @param {number} timestamp
     * @return {string}
     */
    get(key, timestamp) {
        if (this.keyStore.has(key) ) {
            const timestampArray = this.keyStore.get(key);
            for (let i = timestamp; i > 0; i--) {
                if (timestampArray[i]) {
                    return timestampArray[i];
                }
            }
        }
        return "";
    }
}
