import psutil
print "{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format('COMMAND','PID','TID','USER','FD','NAME')
for proc in psutil.process_iter():
        try:
                pinfo = proc.as_dict(attrs=['name','pid','ppid','username','num_fds','exe'])
        except psutil.NoSuchProcess:
                pass
        else:
                for v in pinfo:
                        print "{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(pinfo.get("name"), pinfo.get("pid"),pinfo.get("ppid"), pinfo.get("username"), pinfo.get("num_fsd"), pinfo.get("exe"))
