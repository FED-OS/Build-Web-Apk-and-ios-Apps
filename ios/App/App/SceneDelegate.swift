import UIKit
import Capacitor

class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    var window: UIWindow?

    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
        guard let windowScene = scene as? UIWindowScene else { return }

        window = UIWindow(windowScene: windowScene)
        window?.rootViewController = CAPBridgeViewController()
        window?.makeKeyAndVisible()

        // Forward deep-link URLs opened at launch.
        if let urlContext = connectionOptions.urlContexts.first {
            SceneDelegateProxy.shared.scene(scene, openURLContexts: connectionOptions.urlContexts)
            _ = urlContext
        }

        SceneDelegateProxy.shared.scene(scene, willConnectTo: session, options: connectionOptions)
    }

    func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
        // Deep-link handling: pass the opened URL to the Capacitor App plugin
        // so JS can listen via App.addListener('appUrlOpen').
        SceneDelegateProxy.shared.scene(scene, openURLContexts: URLContexts)
    }

    func scene(_ scene: UIScene, continue userActivity: NSUserActivity) {
        // Universal Links.
        SceneDelegateProxy.shared.scene(scene, continue: userActivity)
    }
}
