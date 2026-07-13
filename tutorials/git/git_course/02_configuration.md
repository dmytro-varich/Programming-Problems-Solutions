# 02. Configuration

Настройка Git а уровне системы, пользователя или отдельного репозитория.

## Уровни конфигурации

Git использует три уровня конфигурации.

| Уровень | Область действия | Файл |
|---------|------------------|------|
| System | Все пользователи системы | `/etc/gitconfig` (Linux/macOS) или `C:\Program Files\Git\etc\gitconfig` (Windows) |
| Global | Текущий пользователь | `~/.gitconfig` или `%USERPROFILE%\.gitconfig` |
| Local | Текущий репозиторий | `.git/config` |

**Приоритет применения настроек:**

```
Local
  ↑
Global
  ↑
System
```

## Просмотр конфигурации

### Все настройки

```bash
git config --list
```

...

### Значение конкретного параметра

```bash
git config <attribute>
```

**Пример:**

```bash
git config user.name
git config user.email
```

### Откуда была загружена настройка

```bash
git config --lost --show-origin
```

Показывает значение параметров и путь к конфигурационному файлу.

...
