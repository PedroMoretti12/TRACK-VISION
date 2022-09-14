import Router from "express";
import express from "express";
import path from "path";

const router = Router()

router.get("/", (req, res) => {
    res.sendFile(path.resolve("site/public/view/index.html"))
})

router.get('/')

export default router;