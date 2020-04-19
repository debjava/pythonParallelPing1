from util import FileUtil
from util import PingUtil
from timeit import default_timer as timer
from multiprocessing import Pool

'''
Created on Apr 19, 2020

@author: debad
'''
NO_OF_PROCESS = 200


def checkAllIpsFromFileParallel(fileName):
    ips = FileUtil.readIPsFromFile(fileName)
    pool = Pool(processes=NO_OF_PROCESS)
    result = pool.map_async(getIPPingStatus, ips)
#     print(result.get())
    pool.close()
    dataList = result.get()
#     print("======>", type(result.get()))
    for i in dataList:
        print(i)

        
def checkAllIpsFromFileSequentially(fileName):
    ips = FileUtil.readIPsFromFile(fileName)
    for ip in ips:
        pingIP(ip)


def pingIP(ip):
    flag = PingUtil.isIPReachable(ip);
    formattedOut = '%16s : %s' % (ip, flag)
    print(formattedOut)

    
def getIPPingStatus(ip):
    flag = PingUtil.isIPReachable(ip);
    formattedOut = '%16s : %s' % (ip, flag)
    return formattedOut


if __name__ == '__main__':
    start = timer()
    checkAllIpsFromFileSequentially("testData/ipaddress-500.txt")
#     checkAllIpsFromFileParallel("testData/ipaddress-500.txt")
    end = timer()
    
    result = end - start
    print("Total Time Taken: ", result, " seconds")
