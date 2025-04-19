# SubHawk - Advanced Subdomain Discovery Tool 🦅

SubHawk is a powerful subdomain and website reconnaissance tool designed for pentesters and bug bounty hunters. It helps discover subdomains of a target domain using customizable wordlists and multi-threading capabilities.

## Features ✨

- Fast subdomain enumeration
- Multi-threading support
- Custom user-agent configuration
- Verbose output mode
- Adjustable request timeout
- Output file support

## Installation 🔧

```bash
git clone https://github.com/yourusername/subhawk.git
cd subhawk
pip install -r requirements.txt
```

## Usage 🚀

Basic usage:
```bash
python3 main.py -d example.com -w wordlist.txt
```

### Arguments

| Flag | Description | Example |
|------|-------------|---------|
| `-d`, `--domain` | Target domain | `--domain example.com` |
| `-w`, `--wordlist` | Path to wordlist | `--wordlist /path/to/wordlist.txt` |
| `-t`, `--threads` | Number of threads (default: 5) | `--threads 10` |
| `--user-agent` | Custom user agent | `--user-agent "Mozilla/5.0"` |
| `-o`, `--output` | Output file path | `--output results.txt` |
| `-v`, `--verbose` | Enable verbose output | `--verbose` |
| `--timeout` | Request timeout in seconds | `--timeout 5` |

### Example Commands

Basic scan:
```bash
python3 main.py -d example.com -w wordlist.txt
```

Advanced scan with all options:
```bash
python3 main.py -d example.com -w wordlist.txt -t 10 --user-agent "CustomAgent/1.0" -o results.txt -v --timeout 5
```

## ⚠️ Disclaimer

This tool is provided for educational and professional security testing purposes only. The user assumes all responsibility for the use of this tool. The developer(s) are not responsible for any misuse, damage, or illegal activities conducted with this tool. Always ensure you have explicit permission to test any domains or systems.

## License 📝

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing 🤝

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## Support 💪

If you find this tool useful, please consider giving it a star ⭐️

---
Made with ❤️ by Linkan333