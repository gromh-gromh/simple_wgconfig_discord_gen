CONFIG_TEMPLATE_PATH = 'config_template.conf'
OUTPUT_FILE_PATH = 'discord.conf'

MAIN_IP_FILE_PATH = 'ip_lists/discord-main-ip-list.txt'
VOICE_IP_FILE_PATH = 'ip_lists/discord-voice-ip-list.txt'

IP_LIST_TAG = 'IP_LIST'

def main():
    with open(MAIN_IP_FILE_PATH, 'r') as main_ip_file:
        main_ips = ','.join(main_ip_file.read().split('\n'))

    with open(VOICE_IP_FILE_PATH, 'r') as voice_ip_file:
        voice_ips = ','.join(voice_ip_file.read().split('\n'))

    with open(CONFIG_TEMPLATE_PATH, 'r') as config_template_file:
        config_template = config_template_file.read()

    full_ip_list = f"{main_ips}{voice_ips}"[0:-1]
    generated_config = config_template.replace(IP_LIST_TAG, full_ip_list)

    with open(OUTPUT_FILE_PATH, 'w') as output_file:
        output_file.write(generated_config)


if __name__ == "__main__":
    main()