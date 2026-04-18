class LoginRequiredMixin:
    def teruskan(self):
        if not self.is_logged_in():
            print("Akses ditolak! User belum login.")
            return
        print("Login berhasil")
        super().teruskan()


class PermissionRequiredMixin:
    def teruskan(self):
        if not self.has_permission():
            print("Akses ditolak! Tidak punya permission.")
            return
        print("Permission valid")
        super().teruskan()


class BaseView:
    def teruskan(self):
        print("Berhasil! Halaman ditampilkan.")


class MyView(LoginRequiredMixin, PermissionRequiredMixin, BaseView):
    def is_logged_in(self):
        return True   # ubah jadi False buat test belum login

    def has_permission(self):
        return True   # ubah jadi False buat test tidak punya izin


# 🔍 LIHAT MRO
print("=== MRO MyView ===")
print([cls.__name__ for cls in MyView.__mro__])

# 🚀 JALANKAN
print("\n=== Test MyView ===")
view = MyView()
view.teruskan()