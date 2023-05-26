from routers import bookingRouter, companyRouter, platformRouter, userRouter, adminRouter

modules = [bookingRouter, companyRouter, platformRouter, userRouter, adminRouter]
routers = [module.router for module in modules]
