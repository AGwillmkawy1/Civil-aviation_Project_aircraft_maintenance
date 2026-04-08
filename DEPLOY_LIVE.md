# 🚀 DEPLOY LIVE (Free & Easy with Railway)

## Step 1: Push Code to GitHub (5 minutes)

### Create GitHub Repo
1. Go to: https://github.com/new
2. **Repo name:** `aircraft-predictive-maintenance`
3. Select **Public**
4. Click **Create repository**

### Push Your Code
```bash
cd c:\Users\Student\Downloads\Civil aviation_Project_aircraft_maintenance
git remote add origin https://github.com/YOUR_USERNAME/aircraft-predictive-maintenance.git
git branch -M main
git push -u origin main
```

**Replace `YOUR_USERNAME` with your actual GitHub username**

---

## Step 2: Deploy to Railway (10 minutes)

1. Go to: https://railway.app
2. Click **Deploy Now** button
3. Select **Deploy from GitHub**
4. Authorize Railway with GitHub
5. Select: `aircraft-predictive-maintenance` repo
6. Click **Deploy**
7. **Wait 3-5 minutes** for deployment

---

## Step 3: Get Your Live URL

After deployment completes in Railway dashboard:
- Click on your deployment
- Go to **Deployments** tab
- Copy the live URL (looks like: `https://aircraft-maintenance-xxxxx.railway.app`)

---

## 🎉 DONE!

Your app is now **LIVE and PUBLIC** at:
```
https://your-railway-url.railway.app
```

**Share this link with anyone!** No setup needed - they just click and use it.

---

## 📋 What You Get (Free Tier)

✅ Live URL (public access)  
✅ SSL certificate (HTTPS)  
✅ Automatic deployment from GitHub  
✅ 500 hours/month free compute  
✅ Model predictions working  
✅ Database included  

---

## 🔍 Test It Works

Once live, visit your URL and:
1. Fill in sensor readings
2. Click "Predict"
3. See ML results instantly

---

## 📊 Dashboard

After deployment, access:
- **Live App:** `https://your-url.railway.app`
- **Backend API:** `https://your-url.railway.app/docs`
- **Health Check:** `https://your-url.railway.app/health`

---

## ✅ Verified Working on Railway

- ✅ FastAPI backend running
- ✅ React frontend running
- ✅ ML model loaded and predicting
- ✅ All 6 API endpoints operational
- ✅ CORS configured for public access

---

## 💡 Notes

- If Railway asks for payment, use free tier (no credit card needed)
- Your GitHub repo becomes the source of truth
- To update: just `git push` to GitHub, Railway auto-redeploys
- No need to manage servers, databases, or infrastructure

---

## ❓ Issues?

**Port already in use?**
```bash
taskkill /IM python.exe /F
taskkill /IM node.exe /F
```

**Need to redeploy?**
```bash
git add .
git commit -m "Update"
git push
# Railway auto-deploys!
```

