from napalm import get_network_driver
driver = get_network_driver('ios')
device = driver('192.168.126.141', 'hocine', 'bbb')
device.open()

device.load_merge_candidate(filename='31_config')
print (device.compare_config())


if len(device.compare_config()) >  0:
    choice = input("\nWould you like to commit these changes? [yN]: ")
    if choice == 'y':
        print('Committing ...')
        device.commit_config()
    else:
        print('Discarding ...')
        device.discard_config()
else:
    print ('No difference')

device.close()
print('Done.')
