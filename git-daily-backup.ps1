cd "C:\Users\MatthewBransgrovesBr\Documents\BransgrovesPortal"

# Check for uncommitted changes
if (git status --porcelain) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
    git add .
    git commit -m "Automated daily backup: $timestamp"
    git push origin main
}
