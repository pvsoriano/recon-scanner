import nmap
import optparse

# nmap scan function; performs a TCP scan and shows the state of each port
def nmapScan(targetHost, targetPort):
	nmScan = nmap.PortScanner()
	nmScan.scan(targetHost, targetPort)
	state=nmScan[targetHost]['tcp'][int(targetPort)]['state']
	print(" [*] " + targetHost + " tcp/" +targetPort +" " +state)

def main():
	parser = optparse.OptionParser('usage%prog '+ '-H <target host> -p <target port>')
	parser.add_option('-H', dest='targetHost', type='string', help='specify target host')
	parser.add_option('-p', dest='targetPort', type='string', help='specify target ports separated by commas')
	(options, args) = parser.parse_args()
	targetHost = options.targetHost
	targetPorts = str(options.targetPort).split(',')
	if (targetHost == None) | (targetPorts[0] == None):
		print(parser.usage)
		exit(0)
	for targetPort in targetPorts:
		nmapScan(targetHost, targetPort)
		
if __name__ == '__main__':
	main()
