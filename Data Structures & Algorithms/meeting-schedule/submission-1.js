/**
 * Definition of Interval:
 * class Interval {
 *   constructor(start, end) {
 *     this.start = start;
 *     this.end = end;
 *   }
 * }
 */

class Solution {
    /**
     * @param {Interval[]} intervals
     * @returns {boolean}
     */
    canAttendMeetings(intervals) {
        // Sort the intervals
        // Think about the way the meetings could collide
        // If ending time of meeting is GREATER the starting time of the next meeting they collide
        // If collide exit loop and return false
        // If collide false then return true
        intervals.sort((interval1, interval2) => interval1.start - interval2.start);
        for(let i = 0; i < intervals.length-1; i++) {
            let [currMeeting, nextMeeting] = [intervals[i], intervals[i+1]];
            if(currMeeting.end > nextMeeting.start) {
                return false;
            }
        }
        return true;;
    }
}
