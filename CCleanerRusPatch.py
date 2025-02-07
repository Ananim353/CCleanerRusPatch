import winreg
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def change_registry_values():
    key_path = r"SOFTWARE\Piriform\CCleaner"
    values_to_change = ["(Cfg)PC", "(Cfg)PE"]
    
    try:
        key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            key_path,
            0,
            winreg.KEY_WRITE
        )
        
        for value_name in values_to_change:
            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, "0")
            print(f"Значение {value_name} успешно изменено на 0")
            
        winreg.CloseKey(key)
        return True
    
    except WindowsError as e:
        print(f"Ошибка при работе с реестром: {str(e)}")
        return False

if __name__ == "__main__":
    try:
        if not is_admin():
            print("Скрипт требует запуска с правами администратора!")
            print("Попробуйте запустить снова, выбрав 'Запуск от имени администратора'")
        else:
            if change_registry_values():
                print("Все изменения успешно применены!")
            else:
                print("Не удалось внести изменения")
                
    except Exception as e:
        print(f"Непредвиденная ошибка: {str(e)}")
    
    #Да это говно код. Вопросы?
    input("\nОкно скрипта может быть закрыто (нажмите Enter для выхода)...")