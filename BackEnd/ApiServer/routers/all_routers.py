from routers import bookingRouter, companyRouter, platformRouter, userRouter

modules = [bookingRouter, companyRouter, platformRouter, userRouter]
routers = [module.router for module in modules]
