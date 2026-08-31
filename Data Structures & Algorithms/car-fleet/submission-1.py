class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        # can catch up before or at destination:
        # (target-front_position) / front_speed >= (target-back_position) / back_speed
        # position_speed = [(position[i], speed[i]) for i in range(n)]
        # or
        position_speed = list(zip(position, speed)) # zip() stops safely at the length of the shorter list, cleaner, faster, and automatically handles the length of the lists
        position_speed.sort(key=lambda x: x[0], reverse=True) # sort in descending order ensures clarity about the final speed of each car
        # iterate over this position_fleet array, maintain a stack for the time of each car reach the target, check if current car's time is less than or equal to the top of the stack, it joins the same fleet, otherwise it forms a new fleet then push its time onto the stack(since the back car cannot pass the car in front of it, so only need to check the one top element in the stack)
        # the length of the stack at the end represents the total number of fleets formed
        time_stack = []
        for ps in position_speed:
            cur_time = (target - ps[0]) / ps[1]
            if len(time_stack) == 0 or cur_time > time_stack[-1]:
                time_stack.append(cur_time)
        
        return len(time_stack)


