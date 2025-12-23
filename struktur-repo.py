import requests

def get_repo_tree(owner, repo, branch="main"):
    """
    Mengambil struktur pohon file dari repositori GitHub publik.
    """
    api_url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            if 'tree' in data:
                print(f"Struktur Repositori: {owner}/{repo} ({branch})\n" + "="*50)
                for item in data['tree']:
                    # Menentukan tipe (blob=file, tree=folder)
                    type_icon = "📁" if item['type'] == 'tree' else "📄"
                    print(f"{type_icon} {item['path']}")
                print("="*50)
                print("\n[INSTRUKSI]: Salin hasil output di atas dan tempelkan ke chat AI.")
            else:
                print("Repositori ditemukan tetapi struktur kosong.")
        elif response.status_code == 404:
            print("Repositori tidak ditemukan. Pastikan nama user dan repo benar dan bersifat Publik.")
        else:
            print(f"Gagal mengakses API. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# --- KONFIGURASI ---
user_github = "jackund25"
nama_repo = "all-about-me"
branch = "main" # Ganti ke 'master' jika branch utama Anda bukan 'main'

# Jalankan fungsi
get_repo_tree(user_github, nama_repo, branch)