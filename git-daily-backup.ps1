cd "C:\Users\MatthewBransgrovesBr\Documents\BransgrovesPortal"

# Check for uncommitted changes
if (git status --porcelain) {
    \ = Get-Date -Format "yyyy-MM-dd HH:mm"
    git add .
    git commit -m "Automated daily backup: \"
    git push origin main
}
