# O(nlog(n)) time | O(1) space
def optimalFreelancing(jobs):
    # Write your code here.
    jobs.sort(key=lambda job: job['payment'], reverse=True)
    max_period = 7
    profit = 0
    week = [True] * max_period

    for job in jobs:
        job_deadline = job['deadline']
        job_payment = job['payment']
        max_time = min(job_deadline, max_period)
        for day in reversed(range(max_time)):
            if week[max_time-1]:
                # print(max_time, week)
                week[max_time-1] = False
                profit += job_payment
                break
    return profit
